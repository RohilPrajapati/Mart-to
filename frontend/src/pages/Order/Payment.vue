<template>
  <div style="width:80%;margin:10px auto">
    <div class="q-my-md">
      <div class="text-h3 text-center q-my-md">Payment</div>
      <div class="text-h5 text-center">Shipping Detail</div>
      Delivery to : {{ this.payment.username }}
      <br />
      Delivery Address : {{ this.payment.address }}
      <br />
      Contact Number : {{ this.payment.contact }}
    </div>
    <div class="q-my-md">
      <div class="text-h5 text-center">Order Items</div>
      <q-markup-table :separator="separator" flat bordered class style="width:100%">
        <thead class="text-white bg-grey">
          <tr>
            <th>Image</th>
            <th>Name</th>
            <th>Price</th>
            <th>quantity</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in this.payment.order_item" :key="item.id">
            <td>
              <q-img
                :src="url_backend+item['product'].image"
                spinner-color="white"
                contain
                style="height: 120px; max-width: 140px; min-width:120px"
              />
            </td>
            <td>{{item['product'].name}}</td>
            <td>Rs. {{item['price']}}</td>
            <td>{{item['quantity']}}</td>
          </tr>
        </tbody>
      </q-markup-table>
      <div class="text-right q-ma-sm">
        <span class="text-bold">Total Payable Amount :</span>
        Rs. {{this.payment.total_amt}}
      </div>
    </div>
    <div class="text-right">
      <form action="https://uat.esewa.com.np/epay/main" method="POST">
        <input :value="this.payment.total_amt" name="tAmt" type="hidden" />
        <input :value="this.payment.total_amt" name="amt" type="hidden" />
        <input value="0" name="txAmt" type="hidden" />
        <input value="0" name="psc" type="hidden" />
        <input value="0" name="pdc" type="hidden" />
        <input value="EPAYTEST" name="scd" type="hidden" />
        <input :value="this.payment.payment_uid" name="pid" type="hidden" />
        <input
          value="http://localhost:8080/#/payment/success?q=su"
          type="hidden"
          name="su"
        />
        <input
          value="http://localhost:8080/#/payment/fail/?q=fu"
          type="hidden"
          name="fu"
        />
        <input
          style="color:white; background-color:green; border-radius: 5px; border:none;padding:5px 20px"
          value="Pay"
          type="submit"
        />
      </form>
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
      separator: 'cell'
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
      if ((this.user_id != this.payment.order_by) || this.payment.payment_status){
        this.$router.push({ name: "error" });
      }
    },
  },
};
</script>

<style>
</style>