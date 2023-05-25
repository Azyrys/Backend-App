<template>
    <div class="main-page">
    <h1>Welcome to the Forum</h1>

    <!-- Register and Login buttons -->
    <div v-if="!loggedIn" class="login-page">
    <div class="buttons">
      <router-link to="/register" class="button">Register</router-link>
      <router-link to="/login" class="button">Login</router-link>
    </div>
  </div>
  <div v-else>
      <!-- Display a message or redirect to main page -->
      <p>You are already logged in.</p>
      <button @click="logout" class="button">Logout</button>
  </div>
    <!-- Forum topics -->
    <div class="forum-topics">
      <h2>Topics</h2>
      <ul>
        <li v-for="topic in topics" :key="topic.id">
          <router-link :to="'/topic/' + topic.id">{{ topic.title }}</router-link>
        </li>
      </ul>
    </div>
  <div>
    <h2>Topics</h2>
    <ul>
      <li v-for="topic in topics" :key="topic.id">
        <h3>Topic Name: {{ topic.title }}</h3>
        <h5>Posts:</h5>
        <ul>
          <li v-for="post in topic.posts" :key="post.id">
            {{ post.content }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
  </div>
</template>
<style scoped>
.main-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.buttons {
  margin-top: 30px;
  display: flex;
  justify-content: center;
}

.button {
  display: inline-block;
  padding: 12px 24px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  font-size: 16px;
  transition: background-color 0.3s;
  margin-right: 10px;
}

.button:last-child {
  margin-right: 0;
}

.button:hover {
  background-color: #0056b3;
}
</style>
<script>
import axios from 'axios';
const apiClient = axios.create({
  baseURL: 'http://localhost:5000', // Update with your backend API URL
  headers: {
    'Content-Type': 'application/json'
  }
})
export default {
  created() {
    // Check if the user is already logged in
    const loggedIn = localStorage.getItem('loggedIn');
    if (loggedIn && this.$store.state.loggedIn === false) {
      // Update the Vuex store with the login status
      this.$store.commit('setLoggedIn', JSON.parse(loggedIn));
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.loggedIn;
    }
  },
  data() {
    return {
      topics: []
    };
  },
  mounted() {
    this.fetchTopics();
  },
  methods: {
    logout() {
      this.$store.dispatch('logout');
    },
    async fetchTopics() {
      try {
        const response = await apiClient.get('/posts');
        console.log(response.data);
        const mergedMap = new Map();

        response.data.forEach(topic => {
          const id = topic[2];
          const title = topic[3];
          const postId = topic[0];
          const content = topic[1];
          if (mergedMap.has(id)) {
            mergedMap.get(id).posts.push({ id: postId, content });
          } else {
            mergedMap.set(id, { id, title, posts: [{ id: postId, content }] });
          }
        });

        const mergedTopics = Array.from(mergedMap.values());
        this.topics = [...mergedTopics];

        console.log(this.topics);
      } catch (error) {
        console.error(error);
      }
    }
  },
};
</script>

<style scoped>
.main-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.forum-topics,
.recent-posts {
  margin-bottom: 30px;
}

.forum-topics h2,
.recent-posts h2 {
  margin-bottom: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 5px;
}

a {
  color: #000;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
