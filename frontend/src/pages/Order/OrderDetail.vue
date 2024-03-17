<template>
  <div class="q-ma-xl">
    <div class="q-my-md">
      <div class="text-h3 text-center q-my-md">Order Detail</div>
      <div class="text-h5 text-center">Shipping Detail</div>
      Delivery to : {{ payment.username }}
      <br />
      Delivery Address : {{ payment.address }}
      <br />
      Contact Number : {{ payment.contact }}
    </div>
    <div class="text-h5 text-center">Order Item</div>
    <div class="row bg-grey-3 q-pa-sm">
      <div class="col-3 text-center">Image</div>
      <div class="col-3 text-center">Name</div>
      <div class="col-3 text-center">Price</div>
      <div class="col-3 text-center">Quantity</div>
    </div>
    <div v-for="item in payment.order_item" :key="item.id" class="row q-my-md">
      <div class="col-3">
        <q-img
          :src="url_backend+item['product'].image"
          spinner-color="white"
          contain
          style="height: 120px; max-width: 140px; min-width:120px"
        />
      </div>
      <div class="col-3">{{item['product'].name}}</div>
      <div class="col-3">Rs. {{item['price']}}</div>
      <div class="col-3">{{item['quantity']}}</div>
    </div>
    <div class="text-right q-ma-sm">
        Total Amount : <span class="text-bold"> {{ payment.total_amt }} </span>
    </div>
    <div class="text-right" v-if="payment.payment_method == 'online' && !payment.payment_status">
        <q-btn color="green-5" @click="$router.push({name:'payment',query:{id:payment.id}})" label="Pay Now" />
    </div>
  </div>
</template>

<script>
import { Store } from "../../store/index";
import { getPayment } from "./api/calls";
import { API_HOST } from "../../config/index";
export default {
  data() {
    return {
      user_id: Store.state.user.user.user_id,
      payment_id: this.$route.query.id,
      payment: {},
      url_backend: API_HOST,
      separator: "cell",
    };
  },
  created() {
    this.get_payment();
  },
  methods: {
    async get_payment() {
      await getPayment(this.payment_id).then((data) => {
        this.payment = data.data.data;
        this.checkSelfUser();
      });
    },
    checkSelfUser() {
      if (this.user_id != this.payment.order_by) {
        this.$router.push({ name: "error" });
      }
    },
  },
};
</script>

<style>
</style>