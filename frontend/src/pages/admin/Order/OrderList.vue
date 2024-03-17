<template>
  <div class="q-my-md q-mx-xl">
    <div class="row q-pa-sm bg-grey-5">
      <div class="col-12 text-h5">Filter</div>
      <div class="col-md-4 q-mt-sm">
        <q-select
          class="q-mb-sm"
          dense
          stack-label
          v-model="cancel_status"
          outlined
          :options="cancel_status_option"
          bg-color="white"
          label="Cancel Status Type"
          emit-value
          map-options
        />
      </div>
      <div class="col-md-4 q-mt-sm">
        <q-select
          class="q-mb-sm"
          dense
          stack-label
          v-model="pay_status"
          outlined
          :options="pay_option"
          bg-color="white"
          label="Payment Status"
          emit-value
          map-options
        />
      </div>
      <div class="col-md-4 q-mt-sm">
        <q-select
          class="q-mb-sm"
          dense
          stack-label
          v-model="pay_method"
          outlined
          :options="pay_method_option"
          bg-color="white"
          label="Payment Method"
          emit-value
          map-options
        />
      </div>
      <div class="col-md-4 q-mt-sm">
        <q-select
          class="q-mb-sm"
          dense
          stack-label
          v-model="delivery_status"
          outlined
          :options="delivery_option"
          bg-color="white"
          label="Delivery Status"
          emit-value
          map-options
        />
      </div>
      <div class="col-md-4 q-mt-sm q-mx-sm">
      <q-btn color="primary" @click="get_payment()" label="Filter" />
      </div>
    </div>
    <div class="text-h4 text-center q-my-md">Order List</div>
    <div
      v-if="error_status || payments.length == 0"
      class="bg-grey-5 text-bold text-center q-pa-md"
    >No Order data</div>
    <div v-else>
      <q-markup-table :separator="separator" flat bordered class style="width:100%">
        <thead class="text-white bg-grey">
          <tr>
            <th>Receiver Name</th>
            <th>Delivery Address</th>
            <th>Contact Number</th>
            <th>Total Amount</th>
            <th>Payment Method</th>
            <th>Payment Status</th>
            <th>Delivery Status</th>
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
            </td>-->
            <td>{{ payment.username }}</td>
            <td>{{ payment.address}}</td>
            <td>{{ payment.contact }}</td>
            <td>{{ payment.total_amt }}</td>
            <td>{{ payment.payment_method }}</td>
            <td v-if="payment.payment_status" class="text-green-5">Paid</td>
            <td v-else class="text-red-5">Unpaid</td>
            <td v-if="payment.delivery_status" class="text-green-5">Delivered</td>
            <td v-else>Not Delivered</td>
            <td><q-btn color="primary" @click="$router.push({name:'admin_order_detail',query:{id:payment.id}})" label="Detail" /></td>
            <!-- <td v-if="!payment.delivery_status">
              <q-btn color="primary" label="Delivery" />
            </td>
            <td v-else>
              <q-btn color="red-5" label="Undo Delivery" />
            </td> -->
          </tr>
        </tbody>
      </q-markup-table>
    </div>
  </div>
</template>

<script>
import { getAllPayment } from "./api/calls";
import { Store } from "../../../store/index";
import { API_HOST } from "../../../config/index";
export default {
  data() {
    return {
      user_id: Store.state.user.user.user_id,
      payments: {},
      separator: "cell",
      url_backend: API_HOST,
      error_status: null,
      cancel_status: null,
      cancel_status_option: ["True", "False"],
      pay_status: null,
      pay_option: ["Paid", "Unpaid"],
      pay_method: null,
      pay_method_option: ["Cash", "Online"],
      delivery_status: null,
      delivery_option: ["True", "False"],
    };
  },
  created() {
    this.get_payment();
  },
  methods: {
    async get_payment() {
      await getAllPayment({
        cancel: this.cancel_status,
        p_method: this.pay_method,
        p_status: this.pay_status,
        d_status:this.delivery_status,
      })
        .then((data) => {
          this.payments = data.data.data;
        })
        .catch((error) => {
          this.error_status = true;
        });
    },
  },
};
</script>

<style>
</style>