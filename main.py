import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.DataFrame(
    columns=['Name', 'Continent', 'Country', 'Quota', 'Period', 'Grade', 'Requirement', 'Note', 'Ranking'])

school_code = ['4609',
               '4590',
               '4558',
               '4507',
               '4605',
               '4564',
               '4541',
               '4543',
               '4542',
               '4540',
               '4547',
               '4579',
               '4539',
               '4506',
               '4613',
               '4708',
               '4504',
               '4575',
               '4534',
               '4535',
               '4536',
               '4537',
               '4538',
               '4516',
               '4709',
               '4707',
               '4529',
               '4530',
               '4531',
               '4532',
               '4533',
               '4614',
               '4566',
               '4630',
               '4634',
               '4631',
               '4632',
               '4633',
               '4635',
               '4629',
               '4661',
               '4656',
               '4643',
               '4619',
               '4620',
               '4593',
               '4513',
               '4514',
               '4521',
               '4555',
               '4557',
               '4522',
               '4706',
               '4499',
               '4569',
               '4591',
               '4585',
               '4610',
               '4715',
               '4568',
               '4571',
               '4702',
               '4586',
               '4565',
               '4528',
               '4618',
               '4617',
               '4612',
               '4567',
               '4627',
               '4623',
               '4621',
               '4622',
               '4512',
               '4616',
               '4580',
               '4581',
               '4583',
               '4587',
               '4626',
               '4624',
               '4570',
               '4578',
               '4611',
               '4508',
               '4714',
               '4584',
               '4603',
               '4701',
               '4607',
               '4602',
               '4511',
               '4561',
               '4548',
               '4544',
               '4703',
               '4608',
               '4615',
               '4574',
               '4576',
               '4710',
               '4573',
               '4577',
               '4711',
               '4582',
               '4725',
               '4572',
               '4588',
               '4712',
               '4600',
               '4699',
               '4598',
               '4594',
               '4595',
               '4601',
               '4596',
               '4606',
               '4597',
               '4592',
               '4698',
               '4697',
               '4501',
               '4525',
               '4502',
               '4628',
               '4550',
               '4523',
               '4554',
               '4705',
               '4551',
               '4562',
               '4520',
               '4672',
               '4686',
               '4684',
               '4677',
               '4689',
               '4685',
               '4687',
               '4676',
               '4675',
               '4678',
               '4671',
               '4683',
               '4688',
               '4673',
               '4694',
               '4674',
               '4690',
               '4680',
               '4682',
               '4681',
               '4691',
               '4670',
               '4692',
               '4693',
               '4679',
               '4658',
               '4638',
               '4696',
               '4645',
               '4655',
               '4652',
               '4651',
               '4669',
               '4659',
               '4660',
               '4604',
               '4505',
               '4527',
               '4524',
               '4549',
               '4563',
               '4720',
               '4517',
               '4518',
               '4556',
               '4500',
               '4666',
               '4716',
               '4640',
               '4665',
               '4667',
               '4553',
               '4639',
               '4668',
               '4719',
               '4664',
               '4642',
               '4519',
               '4647',
               '4636',
               '4559',
               '4718',
               '4717',
               '4695',
               '4641',
               '4663',
               '4662',
               '4657',
               '4644',
               '4653',
               '4724',
               '4654',
               '4637',
               '4649',
               '4648',
               '4650',
               '4723',
               '4722',
               '4721',
               '4704',
               '4509',
               '4560',
               '4545',
               '4546',
               '4526',
               '4625',
               '4510',
               '4599',
               '4552',
               '4713',
               '4503']
for count, c in enumerate(school_code):
    url = f'https://stu88.ntust.edu.tw/outboundstudent/overview/detail/sn/{c}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ '
                      '89.0.4389.114 Safari/537.36'
    }
    cookies = {'__cookie_ob_front_apply_program': 'spring2024euo',
               'PHPSESSID': '70997j3ebtjmu20t0ah0r82e26'
               }
    response = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'table_style7'})
    rows = table.find_all('tr')

    # name
    name = rows[0].find_all('td')[1].text.strip()

    # continent & country
    td = rows[1].find_all('td')[1].text.strip()
    pattern_continent = r'(.+?)\s+/.*'
    pattern_country = r'.*?\s+/\s+(.+)'
    continent = re.findall(pattern_continent, td)[0]
    country = re.findall(pattern_country, td)[0]

    # quota
    quota = rows[2].find_all('td')[1].text.strip()

    # period
    period = rows[3].find_all('td')[1].text.strip()

    # grade
    grade = rows[4].find_all('td')[1].text.strip()

    # requirement & note
    requirement = ''
    note = ''
    if len(rows) > 5:
        # requirement
        requirements = rows[5].find_all('td')
        list_r = [r.text.strip() for r in requirements]
        requirement = '\n'.join([f'{list_r[i]} {list_r[i + 1]}' for i in range(2, len(list_r), 2)])

        # note
        notes = rows[-1].find_all('p')
        for n in notes:
            note += n.text
            note += '\n'

    # ranking
    ranking = None
    url_name = name.lower().replace(' ', '-')
    url = f'https://www.topuniversities.com/universities/{url_name}'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Skipping {url}, Status Code: {response.status_code}")
        continue
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {'class': 'badge-description'})
    if div:
        matches = re.findall(r'\b(\d+)', div.text)
        if matches:
            ranking = [int(match) for match in matches][0]

    # insert into dataframe
    df = pd.concat([df, pd.DataFrame({
        'Name': [name],
        'Continent': [continent],
        'Country': [country],
        'Quota': [quota],
        'Period': [period],
        'Grade': [grade],
        'Requirement': [requirement],
        'Note': [note],
        'Ranking': [ranking]
    })], ignore_index=True)

    print(f"{count + 1}/{len(school_code)} finished")

# convert to excel
df.to_excel('exchange-program_NTUST.xlsx', index=False)
