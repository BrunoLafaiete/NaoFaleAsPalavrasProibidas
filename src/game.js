export function shuffle(items, random = Math.random) {
  const result = [...items];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}
export function outcome(action, zeroError, skips) {
  if (action === 'skip' && skips <= 0) return {points: 0, skip: 0, end: false, advance: false};
  return {points: action === 'correct' ? 1 : 0, skip: action === 'skip' ? 1 : 0, end: action === 'wrong' && zeroError, advance: true};
}
export function nextTurn(team, round, rounds) {
  return {team: team === 0 ? 1 : 0, round: team === 0 ? round : round + 1, finished: team === 1 && round >= rounds};
}
export function remaining(deadline, now = Date.now()) { return Math.max(0, Math.ceil((deadline - now) / 1000)); }
