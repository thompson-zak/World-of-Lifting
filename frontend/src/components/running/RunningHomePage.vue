<template>
  <b-container fluid class="powerliftingPageContainer">

    <b-row>

      <b-col cols=1></b-col>

      <b-col cols=10>
        <RunningForm />
      </b-col>

      <b-col cols=1></b-col>

    </b-row>

  </b-container>
</template>

<script>
import RunningForm from './RunningForm.vue';

export default {
  name: 'PowerliftingHomePage',
  components: {
    RunningForm,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
