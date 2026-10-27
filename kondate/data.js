/* =========================================================
   ヨシケイキッチン 献立表データ
   ・毎週の更新はこのファイルだけを編集します（index.html は触らない）
   ・weeks に1週分を追加：start はその週の月曜（YYYY-MM-DD）
   ・値は Googleドライブ PDF のファイルID（URLの /d/ と /view の間）
     または サイト内PDF 'pdf/YYYY-MM-DD_コース.pdf'
   ・まだ無いコースは書かない／空文字にすると「準備中」と表示
   ・過去の週は自動で非表示になるので、消さなくても大丈夫です
   ========================================================= */
window.KONDATE = {
  recipeUrl: 'https://claude.ai/code/artifact/c649812d-3c76-4a01-b2c8-4484e52faea3',
  courses: [
    { key: 'tezukuri',      name: '手づくりおかず',         color: '#CCFFCC' },
    { key: 'kantan',        name: '簡単おかず',             color: '#FFC000' },
    { key: 'chokantan',     name: '超簡単おかず',           color: '#FF9966' },
    { key: 'volume',        name: 'ボリューム手作りおかず', color: '#FF99CC' },
    { key: 'chokantanplus', name: '超簡単プラス',           color: '#B8CCE4' }
  ],
  weeks: [
    { start: '2026-10-05', files: {
      tezukuri: '1e1Q8gJChDLMpbsPMFwTVOeD_f_juW3Cb',
      kantan: '1LuiQK1VJSlUVOXB_fdOJr9xrllqenXQo',
      chokantan: '1-y42A2SF5j-_wd7_Rl71537CmPe4kW9S',
      volume: '18ZxhIUyyUxRE09gExat2lh3XAEOQxnIw',
      chokantanplus: '1hb3s_Z0Liz4009zAQ-AcoH-DKhrq-pwn' } },
    { start: '2026-10-12', files: {
      tezukuri: '1UIqJlB04ndzn7zcUkUZXYfcO8k1tcxhV',
      kantan: '1aem4tp3iiQGFyM1m81EbTl7UlwEwtnTX',
      chokantan: '1yqSPdckLhaFf1Pxv9qZ_YG7cPT8LJYZu',
      volume: '1Nse5LjEsJDdVKA_yPEuUf50nAkKtPElQ',
      chokantanplus: '1r9R_bDe-ak4upNStk-hjSq-2DNrTmc6t' } },
    { start: '2026-10-19', files: {
      tezukuri: '1Ru8mI-UFVcw9OqmKfyxRbuscMpyh_VX1',
      kantan: '1EBTpf3xTU1nC_i7mvUUbipPNfd2qYnMY',
      chokantan: '1lqAoX6Hm5yyazpuIevcTcwO482v95NIY',
      volume: '1O9BtR3D1FaWGqmAKxDQK2NAqETVEH3gb',
      chokantanplus: '1GK3xBMd1ykMbA6unzuPCqFywpVwq4KcN' } },
    { start: '2026-10-26', files: {
      tezukuri: '18_7BAtg_OVaUNkISQlJJENJDIDkBVcYf',
      kantan: '1qXbJsbN1M86oRFpdSwD9OVrA4_LHd7IK',
      chokantan: '1lRphtO-0zVGBeKttjwLsxLYu1zdGtR8d',
      volume: '1riZwiojRGyh3GzHsA8Z9u0KFFscCAUp0',
      chokantanplus: '1k8Y-RYbz0k8zACxiF0Q8-SMN82Q-acr5' } },
    { start: '2026-11-02', files: {
      tezukuri: '1hxx394GUA15-xIXAVPwGg2h9MjzCa7hq',
      kantan: '1c7z5I_Tf7sElVPlxMPUkJRHPbXRXBUAb',
      chokantan: '13bVba4gv4OJMVH8SHj774-TaiLoau1XB',
      volume: '1y3bnbmZECO0YhHoLxm1R1nTr6obxvckw',
      chokantanplus: '1CrAskGx2dKbyp4hKZyhnZZx6qMLzKBVr' } },
    { start: '2026-11-09', files: {
      tezukuri: '1dotdiGx_h_9iftK0bk2fMlJ7SbK1rugN',
      kantan: '12wCLpJZ-3j3sgFl37Kb3u2TgBZnikfpb',
      chokantan: '1fmihb2ai4H46ZJ1T3No71ntlvZenVWAj',
      volume: '1HmWVLZq9K-l-ePWDJ1JbfBSFbqd1L0nz',
      chokantanplus: '1MGdJM_xTkWG-B7shroqutF27tmf4883H' } },
    { start: '2026-11-16', files: {
      tezukuri: 'pdf/2026-11-16_tezukuri.pdf',
      kantan: 'pdf/2026-11-16_kantan.pdf',
      chokantan: 'pdf/2026-11-16_chokantan.pdf',
      volume: 'pdf/2026-11-16_volume.pdf',
      chokantanplus: 'pdf/2026-11-16_chokantanplus.pdf' } },
    { start: '2026-11-23', files: {
      tezukuri: 'pdf/2026-11-23_tezukuri.pdf',
      kantan: 'pdf/2026-11-23_kantan.pdf',
      chokantan: 'pdf/2026-11-23_chokantan.pdf',
      volume: 'pdf/2026-11-23_volume.pdf',
      chokantanplus: 'pdf/2026-11-23_chokantanplus.pdf' } }
  ]
};
