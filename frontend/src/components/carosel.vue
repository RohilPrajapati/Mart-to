<template>
  <div class="q-pa-md">
    <q-carousel
      animated
      v-model="slide"
      navigation
      infinite
      :autoplay="autoplay"
      arrows
      transition-prev="slide-right"
      transition-next="slide-left"
      @mouseenter="autoplay = false"
      @mouseleave="autoplay = true"
    >
      <q-carousel-slide :name="1" img-src="~assets/pic1.jpg" />
      <q-carousel-slide :name="2" img-src="~assets/pic2.jpg" />
      <!-- <q-carousel-slide :name="3" img-src="https://cdn.quasar.dev/img/parallax2.jpg" />
      <q-carousel-slide :name="4" img-src="https://cdn.quasar.dev/img/quasar.jpg" /> -->
    </q-carousel>
  </div>
</template>

<script>
export default {
  data () {
    return {
      slide: 1,
      autoplay: true
    }
  }
}
</script>
