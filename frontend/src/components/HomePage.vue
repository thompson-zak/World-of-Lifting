<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Compare Your Lifts!</h1>
        <hr><br><br>
        <form>
          <label for="squat">Squat:
            <input type="text" id="squat" name="squat">
          </label>
          <br>
          <label for="bench">Bench:
            <input type="text" id="bench" name="bench">
          </label>
          <br>
          <label for="deadlift">Deadlift:
            <input type="text" id="deadlift" name="deadlift">
          </label>
          <br><br>
          <p>What units are your lifts in?</p>
          <label for="lbs">lbs
            <input type="radio" id="lbs" name="lift_units">
          </label>
          <br>
          <label for="kgs">kgs
            <input type="radio" id="kgs" name="lift_units">
          </label>
        </form>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Analyze Lifts!</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomePage',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
