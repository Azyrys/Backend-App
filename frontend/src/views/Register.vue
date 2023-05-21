<template>
  <div class="register-container">
    <form class="register-form">
      <h2 class="form-title">Register</h2>
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="registerData.username" />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="registerData.password" />
      </div>
      <button class="btn-register" @click.prevent="register">Register</button>
    </form>
  </div>
</template>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.register-form {
  width: 400px;
  padding: 40px;
  background-color: #f2f2f2;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.form-title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: bold;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.btn-register {
  display: block;
  width: 100%;
  padding: 12px;
  background-color: #4caf50;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
  text-align: center;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-register:hover {
  background-color: #45a049;
}

</style>


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