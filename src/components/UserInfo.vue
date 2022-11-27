<template>
	<div >
		<p>USERINFO</p>
		<div class="user">
			<div class="user-add">
				<div class="user-add-item">
					<span class="user-add-decorate">用 户 名&nbsp;: </span><input class = "user-add-conetnt" type="text" placeholder="username" v-model="username"> </br>
				</div>
				<div class="user-add-item">
					<span class="user-add-decorate">密&nbsp; &nbsp; &nbsp; 码：</span> <input class = "user-add-content" type="text" placeholder="password" v-model="password"></br>
				</div>
				<div class="user-add-item">
					<span class="user-add-decorate">真实姓名：</span> <input class = "user-add-content" type="text" placeholder="realName" v-model="realName"></br>
				</div>
				<div class="user-add-item">
					<span class="user-add-decorate">年&nbsp; &nbsp;&nbsp; 龄： </span> <input class = "user-add-content" type="text" placeholder="age" v-model="age"></br>
				</div>
				<div class="user-add-item">
					<span class="user-add-decorate">身&nbsp; &nbsp;&nbsp; 高： </span> <input class = "user-add-content" type="text" placeholder="height" v-model="height"></br>
				</div>
				<input
				  type="submit" 
				  value="Add" 
				  @click="addUserInfo({ username: username, password: password, realName: realName,
										age:age, height: height})" 
				  :disabled="!username || !password">
			</div>
			<div class="user-display">	
				<div class="userinfo" v-for="(user, index) in userInfos" :key="index">
					<span class="userinfo-item">number: {{index}}</span>
					<span class="userinfo-item">username: {{user.username}}</span>
					<span class="userinfo-item">realName: {{user.realName}}</span>
					<span class="userinfo-item">age: {{user.age}}</span>
					<span class="userinfo-item">height: {{user.height}}</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "UserInfo",
  data() {
	return {
	  username: "",
	  realName: "",
	  age: -1,
	  height: 175.00,
	  password: "",
	};
  },
  computed: mapState({
	userInfos: state => state.userInfos.userInfos,
  }),
  methods: mapActions('userInfos', [
	'addUserInfo',
	'deleteUserInfo'
  ]),
  created() {
	this.$store.dispatch('userInfos/getUserInfos')
  }
};
	
</script>

<style>
	.user{
		background-color: beige;
		width: 100%;
	}
	.user-display{
		background-color: antiquewhite;
		position: absolute;
		width: 60%;
	}
	.userinfo{
		margin-top: 1%;
		width: 50%;
		position: relative;
		left :10%;
		text-align: center;
		white-space: nowrap;
	}
	.userinfo-item{
		margin: 1%;
		font-style: italic;
		font-size: medium;
	}
	.user-add{
		position: absolute;
		background-color: beige;
		left: 65%;
		margin-top: 1%;
		padding: 1%;
	}
	.user-add.content{
		position: relative;
		radius: 5%;
		left: 20%;
	}
	.user-add-decorate{
		font-style: initial;
		
		
	}
	.user-add-item{
	
	}
</style>