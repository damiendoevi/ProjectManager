import axios from '../services/axios-default-config'

class AuthenticationService {
  async login(formData) {
    return axios
      .post('/api/auth/jwt/create', formData)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async logout() {
    return axios
      .post('/api/auth/jwt/destroy/')
      .then(function (response) {
        return response
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async register(formData) {
    return axios
      .post('/api/auth/users/', formData)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async sendResetPasswordLink(formData) {
    return axios
      .post('/api/auth/users/reset_password/', formData)
      .then(function (response) {
        return response
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async resetPasswordConfirm(formData) {
    return axios
      .post('/api/auth/users/reset_password_confirm/', formData)
      .then(function (response) {
        return response
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async editProfile() {
    return axios
      .get('/api/auth/users/me/')
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }
}

export default new AuthenticationService()
