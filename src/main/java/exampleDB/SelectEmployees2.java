package exampleDB;

import java.util.List;

import dao.EmployeesDAO;
import dto.EmployeeDTO;

public class SelectEmployees2 {

	public static void main(String[] args) {

		EmployeesDAO empDAO = new EmployeesDAO();
		List<EmployeeDTO> empList = empDAO.findAll();
		
		for(EmployeeDTO emp : empList) {
			// 取得したデータを出力
			System.out.println("ID:" + emp.getId());
			System.out.println("名前:" + emp.getName());
			System.out.println("年齢:" + emp.getAge() + "\n");
		}

	}

}
