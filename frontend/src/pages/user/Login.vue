<template>
  <LoginForm />
</template>

<script>
import LoginForm from "./components/LoginForm.vue";
import { Store } from "../../store/index";


export default {
  name: "Login",
  data() {
    return {
      user_id: Store.state.user.user.user_id,
    };
  },
  components: { LoginForm },
  created() {
    this.checkLogin();
  },
  methods: {
    checkLogin() {
      console.log("working");
      console.log(this.user_id);
      if (this.user_id) {
        this.$router.push({ name: "home" });
      }
    },
  },
};
</script>
