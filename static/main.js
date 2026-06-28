async function postJson(url, body) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });
  return res.json();
}

async function getJson(url) {
  const res = await fetch(url);
  return res.json();
}

function renderFlow(flow) {
  const el = document.getElementById('flow');
  if (!flow || flow.length === 0) el.textContent = '(empty)';
  else el.textContent = flow.join('\n');
}

document.getElementById('btn-init').addEventListener('click', async () => {
  const resp = await postJson('/api/transaction/initiate', { amount: 100.0 });
  renderFlow(resp.transaction_flow);
});

document.getElementById('btn-process').addEventListener('click', async () => {
  const resp = await postJson('/api/transaction/process', {});
  renderFlow(resp.transaction_flow);
});

document.getElementById('btn-complete').addEventListener('click', async () => {
  const resp = await postJson('/api/transaction/complete', {});
  renderFlow(resp.transaction_flow);
});

document.getElementById('btn-flow').addEventListener('click', async () => {
  const resp = await getJson('/api/transaction/flow');
  renderFlow(resp.transaction_flow);
});

document.getElementById('btn-example').addEventListener('click', async () => {
  const resp = await postJson('/api/example', { amount: 42.42 });
  renderFlow(resp.transaction_flow);
});

// initial load
getJson('/api/transaction/flow').then(r => renderFlow(r.transaction_flow));
