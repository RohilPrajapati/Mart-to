<template>
  <div class="q-ma-xl">
    <div class="q-my-md">
      <div class="text-h3 text-center q-my-md">Order Detail</div>
      <div class="text-h5 text-center">Shipping Detail</div>
      Delivery to : {{ payment.username }}
      <br />
      Delivery Address : {{ payment.address }}
      <br />
      Payment Status : {{ payment.payment_status }}
      <br />
      Payment Method : {{ payment.payment_method }}
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
      Total Amount :
      <span class="text-bold">{{ payment.total_amt }}</span>
    </div>
    <div class="text-right" v-if="! payment.delivery_status">
      <q-btn
        color="primary"
        @click="update_payment()"
        label="Delivered"
      />
    </div>
    <div class="text-right" v-else>
      <q-btn color="red-5" @click="update_payment()" label="Cancel Delivery" />
    </div>
  </div>
</template>

<script>
import { Store } from "../../../store/index";
import { getPayment, updatePayment } from "./api/calls";
import { API_HOST } from "../../../config/index";
export default {
  data() {
    return {
      user_id: Store.state.user.user.user_id,
      payment_id: this.$route.query.id,
      payment: {},
      url_backend: API_HOST,
      separator: "cell"
    };
  },
  created() {
    this.get_payment();
  },
  methods: {
    async get_payment() {
      await getPayment(this.payment_id).then((data) => {
        this.payment = data.data.data;
      });
    },
    async update_payment() {
      await updatePayment(this.payment_id).then((data) => {
        this.payment = data.data.data;
        if (this.payment.delivery_status) {
          this.$q.notify({
            color: "green-5",
            textColor: "white",
            icon: "info",
            message: "Product have been delivered",
          });
        } else {
          this.$q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            message: "Product delivered is Cancel",
          });
        }
      });
    },
  },
};
</script>

<style>
</style>