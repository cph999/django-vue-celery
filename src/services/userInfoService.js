import api from '@/services/api'

export default {
  fetchUserInfo() {
    return api.get(`userinfo/`)
              .then(response => response.data)
  },
  postUserInfo(payload) {
    return api.post(`userinfo/`, payload)
              .then(response => {
				return response.data;
			  })
  },
  deleteUserInfo(userId) {
    return api.delete(`userinfo/${userId}`)
              .then(response => response.data)
  }
}