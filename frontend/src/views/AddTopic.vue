<template>
  <div>
    <h2 class="title">Add New Topic</h2>
    <form @submit.prevent="addNewTopic" class="form">
      <div class="form-group">
        <label for="content" class="label">Content:</label>
        <textarea id="content" v-model="content" class="textarea" required></textarea>
      </div>
      <button type="submit" class="button">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json'
  }
});

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

      apiClient
        .post('/add-topic', TopicData)
        .then(response => {
          console.log(response.data);
          // Handle success, e.g., show a success message or redirect
          this.$router.push('/');
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
.title {
  font-size: 24px;
  margin-bottom: 20px;
}

.form {
  max-width: 400px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 20px;
}

.label {
  display: block;
  font-size: 18px;
  margin-bottom: 10px;
}

.textarea {
  width: 100%;
  height: 30px;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 18px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.button:hover {
  background-color: #0056b3;
}
</style>
