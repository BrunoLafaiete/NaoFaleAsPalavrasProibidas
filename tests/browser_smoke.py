from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':393,'height':852},device_scale_factor=1,is_mobile=True,has_touch=True)
 errors=[]
 page.on('pageerror',lambda error:errors.append(str(error)))
 page.goto('http://127.0.0.1:5173/NaoFale-jogo/')
 page.get_by_role('button',name='Vamos jogar').click()
 assert page.get_by_label('Número de rodadas').input_value()=='10'
 page.get_by_label('Número de rodadas').fill('1')
 page.get_by_role('button',name='Começar partida').click()
 page.get_by_role('button',name='Tudo pronto. Valendo!').click()
 assert page.locator('.card li').count()==5
 first=page.locator('.card h2').inner_text()
 page.get_by_role('button',name='Acertou!').click()
 assert page.locator('.score strong').first.inner_text()=='1'
 assert page.locator('.card h2').inner_text()!=first
 page.wait_for_timeout(350)
 page.get_by_role('button',name='Palavra proibida: descartar carta').click()
 assert page.locator('.card').is_visible()
 assert page.locator('.score strong').first.inner_text()=='1'
 for n in [3,2,1]:
  page.wait_for_timeout(350)
  page.get_by_role('button',name=f'Pular ({n})').click()
 assert page.get_by_role('button',name='Pular (0)').is_disabled()
 page.get_by_role('button',name='Pausar turno').click()
 assert page.locator('.card').count()==0
 page.reload()
 page.get_by_role('button',name='Continuar partida').click()
 assert page.get_by_role('heading',name='Uma pausa.').is_visible()
 page.get_by_role('button',name='Retomar turno').click()
 page.screenshot(path='/tmp/naopode-mobile.png',full_page=True)
 # Expire the actual deadline, then reload the persisted match.
 page.evaluate("""() => { const g=JSON.parse(localStorage.getItem('naopode-v1')); g.deadline=Date.now()-1;localStorage.setItem('naopode-v1',JSON.stringify(g)); }""")
 page.reload();page.get_by_role('button',name='Continuar partida').click()
 page.get_by_role('button',name='Próxima equipe').click()
 assert page.get_by_role('heading',name='Equipe 2',exact=True).is_visible()
 page.get_by_role('button',name='Tudo pronto. Valendo!').click()
 assert page.get_by_role('button',name='Pular (3)').is_enabled()
 page.evaluate("""() => {const g=JSON.parse(localStorage.getItem('naopode-v1'));g.deadline=Date.now()-1;localStorage.setItem('naopode-v1',JSON.stringify(g));}""")
 page.reload();page.get_by_role('button',name='Continuar partida').click()
 page.get_by_role('button',name='Ver resultado').click()
 assert page.get_by_role('heading',name='Equipe 1 venceu!').is_visible()
 page.get_by_role('button',name='Jogar novamente').click()
 page.get_by_role('checkbox').check()
 page.get_by_role('button',name='Começar partida').click()
 page.get_by_role('button',name='Tudo pronto. Valendo!').click()
 page.get_by_role('button',name='Palavra proibida: encerrar turno').click()
 assert page.get_by_role('heading',name='Uma palavra proibida encerrou o turno.').is_visible()
 assert not errors,errors
 print('PASS: mobile layout, scoring, normal errors, skip limit, pause, persistence, expiry, team rotation, final result, zero-error mode; no browser exceptions.')
 browser.close()
