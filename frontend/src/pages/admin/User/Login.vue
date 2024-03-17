<template>
  <q-layout>
    <q-page-container>
      <q-page>
        <div class="text-h5 text-center q-my-xl">Admin Login</div>
        <div class="flex flex-center">
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
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
import Auth from "../../../services/Auth";
import { Store } from "../../../store/index";
export default {
  name: "admin_login",
  data() {
    return {
      user_id: Store.state.user.user.user_id,
      admin: Store.state.user.user.admin,
      user: {
        login_user: "",
        password: "",
      },
    };
  },
  created() {
    this.checkLogin();
  },
  methods: {
    checkLogin() {
      console.log("working");
      console.log(this.admin);
      if (this.admin) {
        this.$router.push({ name: "admindashboard" });
      }
    },
    async login() {
      Auth.attempt(this.user)
        .then((data) => {
          if (!data) {
            return;
          }
          Store.dispatch("user/storeuser", data);
          if (Store.state.user.user.admin) {
            this.$router.push({ name: "admindashboard" });
          } else {
            this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "User is not admin User",
            });
            this.$router.push({name:'profile'})
          }
        })
        .catch(() => {
          this.$q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            message: "Email or Password Wrong",
          });
        });
    },
  },
};
</script>
