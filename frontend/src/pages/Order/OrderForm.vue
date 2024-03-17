<template>
  <q-page>
    <div style="width: 70%; margin: 20px auto" class="text-center">
      <h4>Order Items List</h4>
      <div class="row bg-grey-3 q-pa-sm items-center">
        <div class="col-2">
          <q-img :src="backend+product.image" width="100%" height="150px" contain />
        </div>
        <div class="col-4 text-left">
          <div class="text-bold">{{ product.name }}</div>
        </div>
        <div class="col-2">
          <span class="text-bold">Available Quantity</span>
          <br />
          {{ product.stock }}
        </div>
        <div class="col-3">
          <q-input rounded outlined v-model="quantity" type="number" label="Order Quantity" />
        </div>
        <div class="col-1 text-center text-bold">
          Price
          <br />
          Rs. {{ product.price }}
        </div>
      </div>
      <div class="text-right">
        <span class="text-bold">Total Amount:</span>
        Rs.{{this.total_amount}}
      </div>
      <div
        v-if="checkAvailableQtyLess"
        class="bg-red-1 text-red-5 q-py-md"
      >Order Quantity is greate then Stock Quantity</div>
      <div style="width:60%; margin:10px auto">
        <h4>Order Form</h4>
        <q-input class="q-my-md" rounded outlined v-model="form_data.username" label="Order By" />
        <div class="text-red-5"></div>
        <q-input class="q-my-md" rounded outlined v-model="form_data.contact" label="Contact" />
        <q-input class="q-my-md" rounded outlined v-model="form_data.address" label="Address" />

        <div class="q-gutter-sm">
          <span style="font-size:12">Payment :</span>
          <q-radio
            v-model="form_data.payment_method"
            checked-icon="task_alt"
            unchecked-icon="panorama_fish_eye"
            val="cash"
            label="Cash on Delivery"
          />
          <q-radio
            v-model="form_data.payment_method"
            checked-icon="task_alt"
            unchecked-icon="panorama_fish_eye"
            val="online"
            label="E-sewa"
          />
        </div>
        <div>
          <q-btn
            class="q-mr-md"
            :disable="checkAvailableQtyLess"
            color="primary"
            @click="place_order()"
            label="Order"
          />
          <q-btn color="red-7" @click="$router.go(-1)" label="cancel" />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { fetchProductDetail } from "../product/api/calls";
import { API_HOST } from "../../config";
import { getProfile } from "../user/api/calls";
import { createOrder } from "./api/calls";
import { Store } from "../../store/index";
export default {
  data() {
    return {
      product: {},
      backend: API_HOST,
      u_id: Store.state.user.user.user_id,
      order_item: {},
      form_data: {
        username: "",
        contact: "",
        address: "",
        payment_method: "online",
        order_item: [],
      },
      quantity: null,
    };
  },
  computed: {
    total_amount() {
      return this.quantity * this.product.price;
    },
    checkAvailableQtyLess() {
      if (this.quantity > this.product.stock) {
        return true;
      }
      return false;
    },
  },
  created() {
    this.fetchData(this.u_id);
    this.getProduct();
  },
  methods: {
    async getProduct() {
      // console.log(this.$route.params.id)
      this.p_id = this.$route.params.id;
      // console.log(this.p_id);
      if (this.p_id) {
        const response = await fetchProductDetail(this.p_id, {
          status: "t",
        }).then((data) => {
          this.product = data.data.data;
          // console.log(this.product);
        });
      } else {
        this.$router.push({ name: "error" });
      }
    },
    async fetchData(u_id) {
      const response = await getProfile(u_id)
        .then((data) => {
          this.form_data.username = data.data.username;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async place_order() {
      this.form_data.order_item = [];
      this.order_item = {
        product: this.product.id,
        price: this.product.price,
        quantity: this.quantity,
      };
      this.form_data.order_item.push(this.order_item);
      if (this.quantity == null) {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Quantity is required",
        });
      } else if (this.form_data.username == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Username is required",
        });
      } else if (this.form_data.contact == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Contact is required",
        });
      } else if (this.form_data.address == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Address is required",
        });
      } else {
        try {
          const response = await createOrder(this.form_data);
          if (this.form_data.payment_method == "online") {
            console.log("working");
            console.log(response.data.data.id);
            this.$router.push({
              name: "payment",
              query: { id: response.data.data.id },
            });
          } else {
            this.$q.notify({
              color: "green-5",
              textColor: "white",
              icon: "info",
              message: "Order have been Placed",
            });
            this.$router.push({ name: "my_order" });
          }
        } catch (error) {
          this.$q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            message: "Fail to Place Order",
          });
        }
      }
    },
  },
};
</script>

<style>
</style>