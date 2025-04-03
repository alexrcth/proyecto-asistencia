import { createStore } from 'vuex'
import AuthService from '@/services/auth.service'

export default createStore({
  state: {
    user: null,
    isAuthenticated: !!localStorage.getItem('token')
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    currentUser: state => state.user
  },
  mutations: {
    SET_AUTH(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated
    },
    SET_USER(state, user) {
      state.user = user
    }
  },
  actions: {
    async login({ commit }, { username, password }) {
      const success = await AuthService.login(username, password)
      if (success) {
        commit('SET_AUTH', true)
        return true
      }
      return false
    },
    logout({ commit }) {
      AuthService.logout()
      commit('SET_AUTH', false)
      commit('SET_USER', null)
    },
    async fetchCurrentUser({ commit }) {
      if (localStorage.getItem('token')) {
        const user = await AuthService.getCurrentUser()
        if (user) {
          commit('SET_USER', user)
        }
      }
    }
  }
})