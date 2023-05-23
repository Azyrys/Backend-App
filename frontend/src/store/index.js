import { createStore } from 'vuex'
import axios from 'axios'
import router from '@/router'

const apiClient = axios.create({
  baseURL: 'http://localhost:5000', // Update with your backend API URL
  headers: {
    'Content-Type': 'application/json'
  }
})

const store = createStore({
  state: { loggedIn: false },
  mutations: {
    setLoggedIn(state, loggedIn) {
      state.loggedIn = loggedIn;
      // Store login status in localStorage
      localStorage.setItem('loggedIn', loggedIn);
    },
    initializeStore(state) {
      // Get login status from localStorage on store initialization
      const loggedIn = localStorage.getItem('loggedIn');
      if (loggedIn) {
        state.loggedIn = JSON.parse(loggedIn);
      }
    }
  },
  actions: {
    register({ commit }, userData) {
      apiClient.post('/register', userData)
        .then(response => {
          if (response && response.data) {
            console.log(response.data);
            commit('setLoggedIn', true);
            router.push('/');
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
    login( { commit }, userData) {
      apiClient.post('/login', userData)
        .then(response => {
          if (response && response.data) {
            console.log(response.data);
            commit('setLoggedIn', true);
            router.push('/');
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
    },
    logout({ commit }) {
      // Clear the logged-in status in the store and localStorage
      commit('setLoggedIn', false);
      localStorage.removeItem('loggedIn');
      // Redirect to the login page or any other desired page
      router.push('/login');
    }
  },
  modules: {}
})

export default store