/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    './templates/**/*.{html,js}',
    './static/**/*.js',
    './node_modules/tw-elements/dist/js/**/*.js',
    'node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'pal1':"#FBA1B7",
        'pal2':"#FFD1DA",
        'pal3':"#FFF0F5",
      }
    }
  },
  plugins: [
    require("flowbite/plugin")
  ],
};