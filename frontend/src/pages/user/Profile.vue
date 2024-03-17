<template>
  <q-page>
    <div class="row">
      <div class="bg-grey-3 col-8 q-pa-lg q-ma-lg" rounded>
        Username : {{user.username}} <br />
        Email : {{user.email}}
      </div>
      <div class="bg-grey-3 col-3 q-ma-lg q-pa-lg text-center">
        <q-btn @click="$router.push({name:'my_order'})" style="width: 60%" color="grey-9 q-mb-sm" label="My Order" />
        <!-- <q-btn style="width: 60%" color="grey-9 q-mb-sm" label="Pending Payment" /> -->
        <q-btn @click="logoutUser()" style="width: 60%" color="red-9" label="Logout" />
      </div>
    </div>

    <!-- {{user_id}} -->
    <!-- {{token}} -->
  </q-page>
</template>

<script>
import { Store } from '../../store/index'
import { getProfile } from './api/calls'
import { logout } from '../../helpers/index.js'
console.log()
export default {
  name: 'Profile',
  data(){
    return {
        user_id : Store.state.user.user.user_id,
        // token : Store.state.user.auth.access,

        user:{
            username:"",
            email:"",
        }
    }
  },
  created(){
    this.fetchData(this.user_id)
  },
  methods:{
    async fetchData(user_id){
      const response = await getProfile(user_id).then( data => {
            this.user.username = data.data.username
            this.user.email = data.data.email
        }).catch(error => {
            console.log(error)
        })
  },
  logoutUser(){
    logout()
    this.$router.push({name:'login'})
  }
}
}
</script>
