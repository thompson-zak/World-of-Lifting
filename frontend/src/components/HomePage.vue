<template>
  <b-navbar type="dark" variant="light">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
  </b-navbar>
  <PowerliftingHomePage v-if="displayPowerlifting" />
  <StrongmanHomePage v-if="displayStrongman" />
  <div class="cotainer-fluid" v-if="displayHome">
    <div class="row">
      <div class="col">
        <b-img src="@/assets/powerliftingBtn.jpg" style="height:100%" fluid-grow></b-img>
      </div>

      <div class="col">
        <b-img src="@/assets/strongmanBtn.jpg" fluid-grow></b-img>
      </div>
    </div>
  </div>
</template>

<script>
import PowerliftingHomePage from './PowerliftingHomePage.vue';
import StrongmanHomePage from './StrongmanHomePage.vue';

export default {
  name: 'HomePage',
  components: {
    PowerliftingHomePage,
    StrongmanHomePage,
  },
  methods: {},
  data() {
    return {
      displayPowerlifting: false,
      displayStrongman: false,
      displayHome: true,
    };
  },
};
</script>
