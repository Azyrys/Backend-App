<template>
  <div class="login-container">
    <form class="login-form">
      <h2 class="form-title">Login</h2>
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" />
      </div>
      <button class="btn-login" @click.prevent="login">Login</button>
      <button class="btn-register" @click="redirectToRegister">Register</button>
      <button class="btn-register" @click="redirectToMainPage">Register</button>
    </form>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-form {
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

.btn-login {
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

.btn-login:hover {
  background-color: #45a049;
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

</style>


<script>
 import { useToast } from "vue-toastification";
 const toast = useToast();
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      if (!this.username || !this.password) {
        toast.error("Wprowadź nazwę użytkownika i hasło!", {
          position: "top-center",
          timeout: 3000,
          closeOnClick: true,
          pauseOnFocusLoss: true,
          pauseOnHover: true,
          draggable: true,
          draggablePercent: 0.6,
          showCloseButtonOnHover: false,
          hideProgressBar: false,
          closeButton: "button",
          icon: true,
          rtl: false
        });
        return;
      }else{
        this.$store.dispatch('login', {
          username: this.username,
          password: this.password
        });
      }
    },
    redirectToRegister() {
          this.$router.push('register');
    },
    redirectToMainPage() {
          this.$router.push('/');
    }
  }
};
</script>