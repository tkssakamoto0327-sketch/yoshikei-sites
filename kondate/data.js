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
  recipeUrl: 'https://yoshikei-recipe.pages.dev/',
  courses: [
    { key: 'tezukuri',      name: '手づくりおかず',         color: '#CCFFCC' },
    { key: 'kantan',        name: '簡単おかず',             color: '#FFC000' },
    { key: 'chokantan',     name: '超簡単おかず',           color: '#FF9966' },
    { key: 'volume',        name: 'ボリューム手作りおかず', color: '#FF99CC' },
    { key: 'chokantanplus', name: '超簡単プラス',           color: '#B8CCE4' }
  ],
  weeks: [
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
      chokantanplus: 'pdf/2026-11-23_chokantanplus.pdf' } },
    { start: '2026-11-30', files: {
      tezukuri: 'pdf/2026-11-30_tezukuri.pdf',
      kantan: 'pdf/2026-11-30_kantan.pdf',
      chokantan: 'pdf/2026-11-30_chokantan.pdf',
      volume: 'pdf/2026-11-30_volume.pdf',
      chokantanplus: 'pdf/2026-11-30_chokantanplus.pdf' } }
  ]
};
