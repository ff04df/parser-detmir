## parser-detmir

Using https://github.com/yifeikong/curl_cffi for requests

Idea from https://freelance.habr.com/tasks/487473

The parser of https://www.detmir.ru/

## Basic information

* First of all, check **src/config.py**

* Didn't test all 100+ pages on every url

* Could be speeded up by spliting requests in async

* Parses catalogs, splits by catalogs and stores in excel file:

<table>
  <thead>
    <tr>
      <th>Название</th>
      <th>Цена</th>
      <th>Цена с акцией</th>
      <th>Ссылка</th>
    </tr>
  </thead>
    <tbody>
      <tr>
        <td><div dir="auto">H_3</div></td>
        <td><div dir="auto">bgu</div></td>
        <td><div dir="auto">bgs.bgt</div></td>
        <td><div dir="auto">href</div></td>
      </tr>
    </tbody>
</table>
