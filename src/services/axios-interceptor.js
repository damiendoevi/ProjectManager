import axios from './axios-default-config'

const setup = (store) => {
  axios.interceptors.response.use(
    (response) => {
      const requestUrl = response.config.url
      if (requestUrl.includes('api/auth/jwt/create/')) {
        store.dispatch('auth/editProfile')
      }

      return response
    },
    async (error) => {
      const requestUrl = error.config.url
      if (
        !requestUrl.includes('api/auth/jwt/destroy/') &&
        store.state.auth.status.isAuthenticated
      ) {
        if (error.response && error.response.status === 401) {
          if (error.response.data.code && error.response.data.code == 'user_inactive') {
            localStorage.setItem('message', 'user_inactive')
          }
          store.dispatch('auth/reinitializeState')
        }
      }
      return Promise.reject(error)
    }
  )
}

export default setup
