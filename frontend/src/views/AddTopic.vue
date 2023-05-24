<template>
    <div>
      <h2>Add New Topic</h2>
      <form @submit.prevent="addNewTopic">
        <div>
        </div>
        <div>
          <label for="content">Content:</label>
          <textarea id="content" v-model="content" required></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  const apiClient = axios.create({
  baseURL: 'http://localhost:5000', // Update with your backend API URL
  headers: {
    'Content-Type': 'application/json'
  }
})
  export default {
    data() {
      return {
        content: ''
      };
    },
    methods: {
      addNewTopic() {
        const TopicData = {
          content: this.content
        };
  
        apiClient.post('/add-topic', TopicData)
          .then(response => {
            console.log(response.data);
            // Handle success, e.g., show a success message or redirect
          })
          .catch(error => {
            console.error(error);
            // Handle error, e.g., show an error message
          });
      }
    }
  };
  </script>
  
  <style scoped>
  /* Your component-specific styles */
  </style>
  