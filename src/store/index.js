import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import userInfos from './modules/userinfo'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
	userInfos
  }
})