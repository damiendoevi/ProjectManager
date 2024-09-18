import axios from './axios-default-config'

class ProjectService {
  async createProject(formData) {
    return axios
      .post(`/api/projects/`, formData)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async getProjects(url = `/api/projects/`) {
    return axios
      .get(url)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async editProject(projectId) {
    return axios
      .get('/api/projects/' + projectId + '/')
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async updateProject(formData, projectId) {
    return axios
      .patch('/api/projects/' + projectId + '/', formData)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async deleteProject(projectId) {
    return axios
      .delete(`/api/projects/${projectId}/`)
      .then(function (response) {
        return response
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async joinProject(formData) {
    return axios
      .post(`/api/projects/join/`, formData)
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

  async getTasks(projectId) {
    return axios
      .get(`/api/projects/${projectId}/tasks/`)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }

  async createTask(projectId) {
    return axios
      .post(`/api/projects/${projectId}/tasks/`)
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return Promise.reject(error)
      })
  }
}

export default new ProjectService()
