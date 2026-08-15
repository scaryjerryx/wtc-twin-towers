import React, { useEffect, useRef } from 'react';

export const SiteAudio: React.FC = () => {
  const audioCtxRef = useRef<AudioContext | null>(null);

  useEffect(() => {
    // We create the audio context only after user interaction is likely,
    // or just start it and let the browser's autoplay policy handle it.
    // A common workaround is to resume on first click.
    const ctx = new (window.AudioContext || (window as any).webkitAudioContext)();
    audioCtxRef.current = ctx;

    // 1. Distant NYC Traffic (Low-pass filtered brown noise)
    const trafficNoise = ctx.createBufferSource();
    const bufferSize = ctx.sampleRate * 5; // 5 seconds of noise
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    let lastOut = 0;
    for (let i = 0; i < bufferSize; i++) {
      const white = Math.random() * 2 - 1;
      data[i] = (lastOut + (0.02 * white)) / 1.02;
      lastOut = data[i];
      data[i] *= 3.5; // Compensate for gain
    }
    trafficNoise.buffer = buffer;
    trafficNoise.loop = true;

    const trafficFilter = ctx.createBiquadFilter();
    trafficFilter.type = 'lowpass';
    trafficFilter.frequency.value = 300; // Muffled distant city rumble

    const trafficGain = ctx.createGain();
    trafficGain.gain.value = 0.4;

    trafficNoise.connect(trafficFilter);
    trafficFilter.connect(trafficGain);
    trafficGain.connect(ctx.destination);
    trafficNoise.start();

    // 2. Machinery Rumble (Oscillators with LFO)
    const rumbleOsc = ctx.createOscillator();
    rumbleOsc.type = 'sawtooth';
    rumbleOsc.frequency.value = 55; // Low frequency

    const rumbleFilter = ctx.createBiquadFilter();
    rumbleFilter.type = 'lowpass';
    rumbleFilter.frequency.value = 150;

    const rumbleLFO = ctx.createOscillator();
    rumbleLFO.type = 'sine';
    rumbleLFO.frequency.value = 0.5; // Slow pulsing

    const rumbleLFOGain = ctx.createGain();
    rumbleLFOGain.gain.value = 30; // Modulate frequency by 30Hz

    rumbleLFO.connect(rumbleLFOGain);
    rumbleLFOGain.connect(rumbleFilter.frequency);

    const rumbleGain = ctx.createGain();
    rumbleGain.gain.value = 0.2;

    rumbleOsc.connect(rumbleFilter);
    rumbleFilter.connect(rumbleGain);
    rumbleGain.connect(ctx.destination);
    
    rumbleOsc.start();
    rumbleLFO.start();

    // Resume context on first user click to bypass autoplay restrictions
    const resumeAudio = () => {
      if (ctx.state === 'suspended') {
        ctx.resume();
      }
    };
    window.addEventListener('click', resumeAudio);
    window.addEventListener('keydown', resumeAudio);

    return () => {
      trafficNoise.stop();
      rumbleOsc.stop();
      rumbleLFO.stop();
      ctx.close();
      window.removeEventListener('click', resumeAudio);
      window.removeEventListener('keydown', resumeAudio);
    };
  }, []);

  return null;
};
