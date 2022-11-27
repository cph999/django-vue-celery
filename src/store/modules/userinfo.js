import userInfoService from '../../services/userInfoService.js'

const state = {
  userInfos: []
}

const getters = {
  userInfos: state => {
    return state.userInfos
  }
}

const actions = {
  getUserInfos ({ commit }) {
    userInfoService.fetchUserInfo()
    .then(userInfos => {
      commit('setUserInfo', userInfos)
    })
  },
  addUserInfo({ commit }, userInfo) {
    userInfoService.postUserInfo(userInfo)
    .then(() => {
      commit('addUserInfo', userInfo)
    })
  },
  deleteUserInfo( { commit }, msgId) {
    userInfoService.deleteUserInfo(msgId)
    commit('deleteUserInfo', msgId)
  }
}

const mutations = {
  setUserInfo (state, userInfos) {
    state.userInfos = userInfos
  },
  addUserInfo(state, userInfo) {
    state.userInfos.push(userInfo)
  },
  deleteUserInfo(state, msgId) {
    state.userInfos = state.userInfos.filter(obj => obj.pk !== msgId)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}