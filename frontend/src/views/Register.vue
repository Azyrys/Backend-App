<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
      </div>
      <div>
        <label for="role">Role:</label>
        <select v-model="role">
          <option value="user">User</option>
          <option value="admin">Admin</option>
        </select>
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      role: 'user'
    };
  },
  methods: {
    register() {
      this.$store.dispatch('register', {
        username: this.username,
        password: this.password,
        role: this.role
      });
    }
  }
};
</script>