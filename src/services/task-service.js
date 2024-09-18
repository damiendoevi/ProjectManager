import axios from './axios-default-config'

class TaskService {
  async editTask(taskId) {
    return axios
      .get('/api/tasks/' + taskId + '/')
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async updateTask(formData, taskId) {
    return axios
      .patch('/api/tasks/' + taskId + '/', formData)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async deleteTask(taskId) {
    return axios
      .delete(`/api/tasks/${taskId}/`)
      .then(function (response) {
        return response
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async getComments(taskId) {
    return axios
      .get(`/api/tasks/${taskId}/comments/`)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async getMembers(formData) {
    return axios
      .get(`/api/projects/members/`, formData)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async createComment(taskId) {
    return axios
      .post(`/api/tasks/${taskId}/comments/`)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }
}

export default new TaskService()
