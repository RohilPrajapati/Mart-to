<template>
  <q-layout view="hHh Lpr lFf">
    <q-header elevated class="nav_bar">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title class="justify-between">
          <a class="logo" @click="$router.push({name:'admindashboard'})">Mart-to</a>
          
        </q-toolbar-title>
        <q-btn
          flat
          dense
          round
          icon="logout"
          aria-label="Menu"
          @click="adminLogout()"
        />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered content-class="bg-grey-1">
      <q-list>
        <q-item-label header class="text-grey-8">Menu</q-item-label>
        <EssentialLink v-for="link in essentialLinks" :key="link.title" v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { Store } from "../store/index";
import { logout } from '../helpers/index.js'
import EssentialLink from "components/EssentialLink.vue";
const linksData = [
  {
    title: "Dashboard",
    caption: "",
    link: "/#/admin/dashboard",
    icon: "dashboard",
  },
  {
    title: "Users",
    caption: "",
    link: "/#/admin/user",
    icon: "group",
  },
  {
    title: "Product",
    caption: "",
    link: "/#/admin/product",
    icon: "checkroom",
  },
  {
    title: "Order",
    caption: "",
    link: "/#/admin/order",
    icon: "local_mall",
  },
];
export default {
  name: "MainLayout",
  components: {
    EssentialLink,
  },
  data() {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData,
      search: null,
      admin: Store.state.user.user.admin,
    };
  },
  created() {
    console.log(this.admin)
    this.isAdmin();
  },
  computed: {
    login() {
      if (Store.state.user.user.user_id) {
        return true;
      }
      return false;
    },
  },
  methods: {
    isAdmin() {
      // console.log(this.admin)
      if (!this.admin) {
        this.$q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            message: "You are not Admin Please Login as Admin",
          });
        this.$router.push({ name: "admin_login" });
      }
    },
    adminLogout(){
      logout()
      this.$router.push({name:'admin_login'})
    }
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=El+Messiri:wght@600&display=swap");
.nav_bar {
  background-color: rgb(221, 221, 221);
  color: black;
}
.logo {
  color: black;
  text-decoration: none;
  font-family: "El Messiri", sans-serif;
}
</style>