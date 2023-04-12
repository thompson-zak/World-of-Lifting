<template>
  <b-navbar type="dark" variant="light">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
  </b-navbar>
  <PowerliftingForm @analyzeLiftsData="onFormSubmit" />
  <PowerliftingResults :liftData="liftData" v-if="shouldLoad"/>
</template>

<script>
import PowerliftingForm from './PowerliftingForm.vue';
import PowerliftingResults from './PowerliftingResults.vue';

export default {
  name: 'HomePage',
  components: {
    PowerliftingForm,
    PowerliftingResults,
  },
  data() {
    return {
      shouldLoad: false,
      liftData: {},
    };
  },
  methods: {
    onFormSubmit(data) {
      // This is where you will update everything with emitted data
      console.log(data);
      this.liftData = data;
      this.shouldLoad = true;
    },
  },
};
</script>
