<template>
  <div>
    <router-link to="/register">Register</router-link>
    <router-link to="/login">Login</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  // ... rest of the component code ...
}
</script>