<template>
  <q-layout view="hHh Lpr lFf">
    <q-header elevated class="nav_bar">
      <q-toolbar>
        <!-- <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />-->

        <q-toolbar-title>
          <a class="logo" v-bind:href="/#/">Mart-to</a>
        </q-toolbar-title>
        <div class="row no-wrap">
          <q-input
            class="q-mr-sm"
            dense
            outlined
            rounded
            @keyup.enter= "$router.push({name:'search',query:{search:search}}).catch(err => {})"
            v-model="search"
            placeholder="Search Product"
          />
          <span>
            <!-- <q-btn rounded color="grey-3" text-color="grey-8" icon="search" @click="$router.push({name:'search',query:{search:search,t: new Date().getTime()}})" unelevated /> -->
            <q-btn rounded color="grey-3" text-color="grey-8" icon="search" @click="$router.push({name:'search',query:{search:search}}).catch(err => {})" unelevated />
          </span>
        </div>
      </q-toolbar>
      <q-tabs align="center">
        <q-route-tab to="/" label="Home" />
        <q-route-tab to="/cart" label="Cart" />
        <q-route-tab v-show="!login" to="/login" label="Login" />
        <q-route-tab v-show="!login" to="/signup" label="Sign Up" />
        <q-route-tab v-show="login" to="/profile" label="Profile" />
      </q-tabs>
    </q-header>

    <!-- <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Menu
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>-->

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { Store } from "../store/index";

// import EssentialLink from 'components/EssentialLink.vue'

export default {
  name: "MainLayout",
  components: {
    // EssentialLink
  },
  data() {
    return {
      leftDrawerOpen: false,
      //essentialLinks: linksData,
      search: this.$route.query.search,
      userId: Store.state.user.user.user_id,
    };
  },
  computed: {
    login() {
      if (Store.state.user.user.user_id) {
        return true;
      }else{
        return false;
      }
    },
    current_page(){
      return this.$route.name
    }
  },
  methods: {
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