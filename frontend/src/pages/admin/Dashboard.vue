<template>
  <div class="q-ma-xl">
    <div class="text-h5">Dashboard</div>
    <div class="row">
      <div class="col-3 bg-green-5 q-pa-md q-ma-sm">
        <div>Total Sales:</div>
        <div style="font-size:26px">Rs. {{ data['total_sales_amt'] }}</div>
      </div>
      <div class="col-3 bg-red-5 q-pa-md q-ma-sm">
        <div>Total Sales Count:</div>
        <div style="font-size:26px">{{ data['total_sales'] }}</div>
      </div>
      <div class="col-3 bg-blue-5 q-pa-md q-ma-sm">
        <div>Total Product Count:</div>
        <div style="font-size:26px">{{ data['total_product'] }}</div>
      </div>
      <div class="col-3 bg-yellow-5 q-pa-md q-ma-sm">
        <div>Total User:</div>
        <div style="font-size:26px">{{ data['total_user'] }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { getDashBoardData } from "./api/calls";
export default {
  data() {
    return {
      data: {},
    };
  },
  created() {
    this.getDashboard();
  },
  methods: {
    async getDashboard() {
      await getDashBoardData()
        .then((data) => {
          this.data = data.data;
        })
        .catch((error) => {
          this.error_status = true;
        });
    },
  },
}
</script>

<style>
.dash_card {
  height: 150px;
  width: 100%;
}
</style>