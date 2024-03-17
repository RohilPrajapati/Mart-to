<template>
  <div class="q-my-md q-mx-xl">
    <div class="text-h4 text-center q-my-md">My Order</div>
    <div v-if="error_status" class="bg-grey-5 text-bold text-center q-pa-md">
        No Order data
    </div>
    <div v-else>
    <q-markup-table :separator="separator" flat bordered class style="width:100%">
      <thead class="text-white bg-grey">
        <tr>
          <th>Receiver Name</th>
          <th>Delivery  Address</th>
          <th>Contact Number</th>
          <th>Total Amount</th>
          <th>Payment Method</th>
          <th>Payment Status</th>
          <th>Delivery Status</th>
          <th>Product</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="payment in this.payments" :key="payment.id">
          <!-- <td>
            <q-img
              :src="url_backend+item['product'].image"
              spinner-color="white"
              contain
              style="height: 120px; max-width: 140px; min-width:120px"
            />
          </td> -->
          <td>{{ payment.username }}</td>
          <td>{{ payment.address}}</td>
          <td>{{ payment.contact }}</td>
          <td>{{ payment.total_amt }}</td>
          <td>{{ payment.payment_method }}</td>
          <td v-if="payment.payment_status" class="text-green-8">Paid</td>
          <td v-else class="text-red-5">Unpaid</td>
          <td v-if="payment.delivery_status">Delivered</td>
          <td v-else>Not Delivered</td>
          <td>
            <!-- {{payment.order_item}} -->
            <div v-for="item in payment['order_item']" :key=item.id>

                {{item.product.name}}
            </div>
          </td>
          <td class="text-center">
            <!-- <q-btn color="green-5" @click="$router.push({name:'payment',query:{id:payment.id}})" label="Pay Now" /> -->
            <q-btn color="primary" @click="$router.push({name:'order_detail',query:{id:payment.id}})" label="Detail" />
          </td>
          <!-- <td>{{item['quantity']}}</td> -->
        </tr>
      </tbody>
    </q-markup-table>
    </div>
  </div>
</template>

<script>
import { getUserWisePayment } from "./api/calls";
import { Store } from "../../store/index"
import { API_HOST } from "../../config/index";
export default {
  data() {
    return {
      user_id: Store.state.user.user.user_id,
      payments: {},
      separator:'cell',
      url_backend: API_HOST,
      error_status:null
    };
  },
  created(){
    this.get_payment();
  },
  methods: {
    async get_payment() {
      await getUserWisePayment(this.user_id).then((data) => {
        this.payments = data.data.data;
        this.checkSelfUser();
      }).catch((error) =>{
        this.error_status=true
      })
    },
    checkSelfUser() {
      if ((this.user_id != this.payments[0].order_by)){
        this.$router.push({ name: "error" });
      }
    },
  },
};
</script>

<style>
</style>