<template>
  <div class="register-container">
    <form class="register-form">
      <h2 class="form-title">Register</h2>
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" />
      </div>
      <div class="form-group">
        <label for="role">Role:</label>
        <select v-model="role" id="role" class="form-control">
          <option value="user">User</option>
          <option value="admin">Admin</option>
        </select>
      </div>
      <button class="btn-register" @click.prevent="register">Register</button>
      <br />
      <button class="btn-login" @click.prevent="redirectToLogin">Login</button>
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
.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

.form-control {
  display: block;
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  color: #495057;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
.btn-register:hover {
  background-color: #45a049;
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
</style>


<script>
 import { useToast } from "vue-toastification";
 const toast = useToast();
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
      if (!this.username || !this.password) {
        toast.error("Wprowadź nazwę użytkownika i hasło!", {
          position: "top-center",
          timeout: 5000,
          closeOnClick: true,
          pauseOnFocusLoss: true,
          pauseOnHover: true,
          draggable: true,
          draggablePercent: 0.6,
          showCloseButtonOnHover: false,
          hideProgressBar: true,
          closeButton: "button",
          icon: true,
          rtl: false
        });
        return;
      }else{
          this.$store.dispatch('register', {
          username: this.username,
          password: this.password,
          role: this.role
        });
      }
    },
    redirectToLogin() {
          this.$router.push('login');
    }
  }
};
</script>