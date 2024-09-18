import AuthenticationService from '../services/authentication-service'
import router from '../router/index.js'

const initialState = { status: { isAuthenticated: false }, user: null }

export const auth = {
  namespaced: true,
  state: initialState,
  actions: {
    login({ commit }, formData) {
      return AuthenticationService.login(formData).then(
        (response) => {
          commit('loginSuccess', response)
          return Promise.resolve(response)
        },
        (error) => {
          commit('loginFailure')
          return Promise.reject(error)
        }
      )
    },
    logout({ commit }) {
      AuthenticationService.logout()
      commit('logout')
    },
    editProfile({ commit }) {
      return AuthenticationService.editProfile().then(
        (response) => {
          commit('editProfileSuccess', response)
        },
        (error) => {
          commit('editProfileFailure', error)
        }
      )
    },
    reinitializeState({ commit }) {
      commit('reinitializeState')
    }
  },
  mutations: {
    loginSuccess(state, user) {
      state.status.isAuthenticated = true
      state.user = user
    },
    loginFailure(state) {
      state.status.isAuthenticated = false
      state.user = null
    },
    logout(state) {
      state.status.isAuthenticated = false
      state.user = null
    },
    editProfileSuccess(state, user) {
      state.status.isAuthenticated = true
      state.user = user
    },
    editProfileFailure(state) {
      state.status.isAuthenticated = false
      state.user = null
    },
    reinitializeState(state) {
      state.status.isAuthenticated = false
      state.user = null
      router.push('/login')
    }
  }
}
