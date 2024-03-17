<template>
  <q-page class="flex flex-center">
    <div class="form" align="center">
      <q-input class="q-mb-sm" rounded outlined v-model="user.login_user" label="Username" />
      <q-input
        class="q-mb-sm"
        rounded
        outlined
        v-model="user.password"
        type="password"
        label="Password"
      />
      <q-btn unelevated rounded color="primary" @click="login()" label="Login" />
    </div>
  </q-page>
</template>
<script>
import Auth from "../../../services/Auth";
import { Store } from "src/store";

export default {
  name: "LoginForm",
  data() {
    return {
      user: {
        login_user: "",
        password: "",
      },
    };
  },
  components: {},
  methods: {
    async login() {
      if (this.user.login_user == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Email/Username is required",
        });
      } else if (this.user.password == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Password is required",
        });
      } else {
        Auth.attempt(this.user)
          .then((data) => {
            if (!data) {
              return;
            }
            Store.dispatch("user/storeuser", data);
            this.$router.push({ name: "profile" });
          })
          .catch((response) => {
            console.log(response.response.message)
            this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "Email or Password Invalid",
            });
          });
      }
    },
  },
};
</script>
<style scoped>
.form {
  width: 350px;
}
</style>