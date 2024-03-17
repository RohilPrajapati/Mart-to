<template>
  <q-page class="flex flex-center">
    <div class="form" align="center">
      <q-input class="q-mb-sm" rounded outlined v-model="user.username" label="Username" />
      <q-input class="q-mb-sm" type="email" rounded outlined v-model="user.email" label="E-mail" />
      <q-input
        class="q-mb-sm"
        rounded
        outlined
        v-model="user.password"
        type="password"
        label="Password"
      />
      <q-input
        class="q-mb-sm"
        rounded
        outlined
        v-model="c_password"
        type="password"
        label="Confirm Password"
      />
      <q-btn unelevated rounded color="primary" @click="validate_submit()" label="Sign Up" />
    </div>
  </q-page>
</template>
<script>
import { createUser } from "../api/calls";

export default {
  name: "SignupForm",
  data() {
    return {
      c_password: "",
      user: {
        email: "",
        username: "",
        password: "",
      },
    };
  },
  methods: {
    async validate_submit() {
      if (this.user.email == ""){
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "E mail cant be empty",
        });
      }
      else if (this.user.username == ""){
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Username cant be empty",
        });
      }
      else if (this.user.password == "" || this.user.c_password == ""){
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Password or Confirm Password cant be empty",
        });
      }
      else if (this.user.password != this.c_password) {
        // console.log("faile")
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Password and Confirm Password do not match",
        });
      } else {
        await createUser(this.user)
          .then(({ data }) => {
            this.$q.notify({
              color: "green-5",
              textColor: "white",
              icon: "info",
              message: "User Have been Registered",
            });
            this.$router.push({ name: "login" });
          })
          .catch((error) => {
            this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "Unable to register",
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