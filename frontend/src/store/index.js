import { createStore } from 'vuex'
import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:5000', // Update with your backend API URL
  headers: {
    'Content-Type': 'application/json'
  }
})

const store = createStore({
  state: {},
  mutations: {},
  actions: {
    register(context, userData) {
      apiClient.post('/register', userData)
        .then(response => {
          if (response && response.data) {
            console.log(response.data);
            // Handle success, e.g., show success message or redirect
          } else {
            console.error('Invalid response data');
            // Handle error, e.g., show error message
          }
        })
        .catch(error => {
          if (error && error.response && error.response.data) {
            console.error(error.response.data);
            // Handle error, e.g., show error message
          } else {
            console.error('Invalid error response');
            // Handle error, e.g., show error message
          }
        });
    },
    login(context, userData) {
      apiClient.post('/login', userData)
        .then(response => {
          if (response && response.data) {
            console.log(response.data);
            // Handle success, e.g., store token in localStorage or redirect
          } else {
            console.error('Invalid response data');
            // Handle error, e.g., show error message
          }
        })
        .catch(error => {
          if (error && error.response && error.response.data) {
            console.error(error.response.data);
            // Handle error, e.g., show error message
          } else {
            console.error('Invalid error response');
            // Handle error, e.g., show error message
          }
        });
    }
  },
  modules: {}
})

export default store