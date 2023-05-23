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
      
      <!-- Recent posts -->
      <div class="recent-posts">
        <h2>Recent Posts</h2>
        <ul>
          <li v-for="post in recentPosts" :key="post.id">
            <router-link :to="'/post/' + post.id">{{ post.title }}</router-link>
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
  methods: {
    logout() {
      this.$store.dispatch('logout');
    }
  },
    data() {
      return {
        topics: [
          { id: 1, title: 'Topic 1' },
          { id: 2, title: 'Topic 2' },
          { id: 3, title: 'Topic 3' }
        ],
        recentPosts: [
          { id: 1, title: 'Post 1' },
          { id: 2, title: 'Post 2' },
          { id: 3, title: 'Post 3' }
        ]
      };
    }
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
  