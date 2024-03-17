<template>
  <div class="q-ma-xl">
    <div class="row no-wrap q-my-lg">
        <q-input class="q-mr-sm" dense outlined rounded @keyup="fetchAllUser()" v-model="search" placeholder="Search User" />
        <!-- <q-btn @click="getProduct()" rounded color="grey-3" text-color="grey-8" icon="search" unelevated /> -->
        <!-- <q-btn class="q-mx-sm" color="primary" @click="$router.push('product/add'); " rounded label="Add New product" /> -->
    </div>
    <div class="text-h5">User List</div>
    <q-markup-table :separator="separator" flat bordered class>
      <thead>
        <tr class="text-white bg-grey">
          <th>Id</th>
          <th>Username</th>
          <th>E-mail</th>
          <th>Admin</th>
          <th>Active</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.user_id">
          <td class="text-left">{{ user.user_id }}</td>
          <td class="text-left">{{ user.username }}</td>
          <td class="text-center">{{ user.email}}</td>
          <td v-if="user.is_superuser" class="text-center text-green-5">Yes</td>
          <td v-else class="text-center text-red-5">No</td>
          <td v-if="user.status" class="text-center text-green-5">Yes</td>
          <td v-else class="text-center text-red-5">No</td>
          <!--<td class="text-left">{{product.description}}</td>
          <td class="text-right">Rs. {{ product.price }}</td>
          <td class="text-center" v-if="product.status">Enabled</td>
          <td class="text-center" v-else>Disabled</td> -->
          <td class="text-center"> 
            <q-btn color="red-7" @click="updateIsActiveUser(user.user_id)" :disable="user.is_superuser" v-if="user.status" label="Disable" />
            <q-btn color="green-7" @click="updateIsActiveUser(user.user_id)"  v-else label="Enable" />
          </td>
        </tr>
      </tbody>
    </q-markup-table>
  </div>
</template>

<script>
import { getAllUser,updateStatusUser } from "./api/calls";
export default {
  data() {
    return {
      users: [],
      separator:'cell',
      search:null
    };
  },
  created(){
    this.fetchAllUser()
  },
  methods: {
    async fetchAllUser() {
      await getAllUser({
        search:this.search
      }).then((response) => {
        this.users = response.data.data;
      });
    },
    async updateIsActiveUser(id) {
      await updateStatusUser(id).then((response) => {
        // this.$router.push({name:'adminUserList'})
        this.fetchAllUser()
      });
    },
  },
};
</script>

<style>
</style>