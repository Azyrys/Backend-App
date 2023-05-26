<template>
  <div>
    <h2>Add New Post</h2>
    <form @submit.prevent="addNewPost" class="new-post-form">
      <div>
        <label for="topic">Topic:</label>
        <select id="topic" v-model="selectedTopic" required>
          <option value="">Select a topic</option>
          <option v-for="topic in topics" :key="topic[0]" :value="topic[1]">
            {{ topic[1] }}
          </option>
        </select>
      </div>
      <div>
        <label for="content">Content:</label>
        <textarea id="content" v-model="content" required></textarea>
      </div>
      <button type="submit" class="submit-button">Submit</button>
    </form>
    <button class="btn-register" @click="redirectToMainPage">Main Page</button>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from "vue-toastification";
 const toast = useToast();
const apiClient = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json'
  }
});

export default {
  data() {
    return {
      selectedTopic: '',
      content: '',
      topics: []
    };
  },

  mounted() {
    this.fetchTopics();
  },

  methods: {
    fetchTopics() {
      apiClient
        .get('/topics')
        .then(response => {
          this.topics = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },

    addNewPost() {
      const postData = {
        topic: this.selectedTopic,
        content: this.content
      };
      if(localStorage.getItem('loggedIn')){
      apiClient
        .post('/add-post', postData)
        .then(response => {
          console.log(response.data);
          // Handle success, e.g., show a success message or redirect
          this.$router.push('/');
          toast.success("Post dodany")
        })
        .catch(error => {
          console.error(error);
          // Handle error, e.g., show an error message
          
        });
    
    }else{
      toast.error("Musisz byc zalogowany")
    }
  },
  redirectToMainPage() {
          this.$router.push('/');
    }
  }
};
</script>

<style scoped>
.new-post-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f5f5f5;
}
.btn-register {
      display: block;
      width: 100%;
      background-color: #4CAF50;
      color: white;
      font-size: 16px;
      font-weight: bold;
      text-align: center;
      border: none;
      padding: 12px;
      border-radius: 4px;
      cursor: pointer;
      margin-top: 10px;
      margin-left: auto;
    }

.btn-register:hover {
  background-color: #45a049;
}
.new-post-form h2 {
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

.new-post-form label {
  display: block;
  margin-bottom: 10px;
  font-size: 16px;
  color: #555;
}

.new-post-form select,
.new-post-form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  font-size: 16px;
  color: #555;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
}

.new-post-form textarea {
  height: 150px; /* Adjust the height as needed */
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  margin-right: 10px; /* Add margin to the right side */
  font-size: 16px;
  color: #555;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  box-sizing: border-box; /* Include padding and border in the width calculation */
}

.new-post-form button {
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.new-post-form button:hover {
  background-color: #0056b3;
}

</style>
