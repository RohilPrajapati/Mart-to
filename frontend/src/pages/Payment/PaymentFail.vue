<template>
  <div>
    <div class="bg-red-5 text-center q-pa-lg">
      <div class="text-h4">Payment Fail</div>
    </div>
    <p class="q-ma-lg text-center">
        <span class="text-bold">Payment have been fail!</span>
        Please try again <br>
        <q-btn class="q-mt-md" @click="$router.push({name:'my_order'})" color="green-5" text-color="white" label="To Pay Again" />
    </p>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>