<script setup>

</script>

<template>
  <svg class="filter">
    <defs style="touch-action: none;">
      <filter id="filter" color-interpolation-filters="sRGB" style="touch-action: none;">
        <!-- the input displacement image -->
        <feImage x="0" y="0" width="110%" height="110%" result="map" href="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPHN2ZyBjbGFzcz0iZGlzcGxhY2VtZW50LWltYWdlIiB2aWV3Qm94PSIwIDAgMTUwMC45ODEgNjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InJlZCIgeDE9IjEwMCUiIHkxPSIwJSIgeDI9IjAlIiB5Mj0iMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiMwMDAiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSJyZWQiLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJsdWUiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjMDAwIi8+CiAgICAgIDxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iYmx1ZSIvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjE1MDEuMDUiIGhlaWdodD0iNjAiIGZpbGw9ImJsYWNrIiBzdHlsZT0iIi8+CiAgPHJlY3Qgd2lkdGg9IjE1MDEuMDUiIGhlaWdodD0iNjAiIHJ4PSIxNiIgZmlsbD0idXJsKCNyZWQpIiBzdHlsZT0iIi8+CiAgPHJlY3Qgd2lkdGg9IjE1MDEuMDUiIGhlaWdodD0iNjAiIHJ4PSIxNiIgZmlsbD0idXJsKCNibHVlKSIgc3R5bGU9Im1peC1ibGVuZC1tb2RlOiBkaWZmZXJlbmNlOyIvPgogIDxyZWN0IHg9IjYuMzA0IiB5PSIyLjEiIHdpZHRoPSIxNDg4LjQ0IiBoZWlnaHQ9IjU1LjgiIHJ4PSIxNiIgZmlsbD0iaHNsKDAgMCUgNTAlIC8gMC45MyIgc3R5bGU9ImZpbHRlcjogYmx1cig3cHgpOyIvPgo8L3N2Zz4=" style="touch-action: none;"></feImage>
        <!-- the displacement map to use -->
        <!-- <feDisplacementMap in2="map" in="SourceGraphic" /> -->
        <!-- the chromatic aberration for the people -->
        <!-- RED channel with strongest displacement -->
        <feDisplacementMap in="SourceGraphic" in2="map" id="redchannel" xChannelSelector="R" yChannelSelector="B" result="dispRed" scale="-160" style="touch-action: none;"></feDisplacementMap>
        <feColorMatrix in="dispRed" type="matrix" values="1 0 0 0 0
                                  0 0 0 0 0
                                  0 0 0 0 0
                                  0 0 0 1 0" result="red" style="touch-action: none;"></feColorMatrix>
        <!-- GREEN channel (reference / least displaced) -->
        <feDisplacementMap in="SourceGraphic" in2="map" id="greenchannel" xChannelSelector="R" yChannelSelector="B" result="dispGreen" scale="-150" style="touch-action: none;"></feDisplacementMap>
        <feColorMatrix in="dispGreen" type="matrix" values="0 0 0 0 0
                                  0 1 0 0 0
                                  0 0 0 0 0
                                  0 0 0 1 0" result="green" style="touch-action: none;"></feColorMatrix>
        <!-- BLUE channel with medium displacement -->
        <feDisplacementMap in="SourceGraphic" in2="map" id="bluechannel" xChannelSelector="R" yChannelSelector="B" result="dispBlue" scale="-140" style="touch-action: none;"></feDisplacementMap>
        <feColorMatrix in="dispBlue" type="matrix" values="0 0 0 0 0
                                  0 0 0 0 0
                                  0 0 1 0 0
                                  0 0 0 1 0" result="blue" style="touch-action: none;"></feColorMatrix>
        <!-- Blend channels back together -->
        <feBlend in="red" in2="green" mode="screen" result="rg" style="touch-action: none;"></feBlend>
        <feBlend in="rg" in2="blue" mode="screen" result="output" style="touch-action: none;"></feBlend>
        <!-- output blend -->
        <feGaussianBlur in="output" stdDeviation="0" style="touch-action: none;"></feGaussianBlur>
      </filter>
    </defs>
  </svg>
</template>

<style scoped>
.filter {
  width: 100%;
  height: 93%;
  pointer-events: none;
  position: absolute;
  inset: 0;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 2.2);
}

.your-element {
  box-shadow: 0 0 2px 1px color-mix(in oklch, canvasText, #0000 65%) inset,
  0 0 10px 4px color-mix(in oklch, canvasText, #0000 85%) inset,
  0px 4px 16px rgba(17, 17, 26, 0.05),
  0px 8px 24px rgba(17, 17, 26, 0.05),
  0px 16px 56px rgba(17, 17, 26, 0.05),
  0px 4px 16px rgba(17, 17, 26, 0.05) inset,
  0px 8px 24px rgba(17, 17, 26, 0.05) inset,
  0px 16px 56px rgba(17, 17, 26, 0.05) inset;
}
</style>