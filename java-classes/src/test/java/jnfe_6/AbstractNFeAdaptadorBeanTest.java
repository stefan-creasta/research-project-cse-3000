
package jnfe_6;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.Before;
import org.junit.Test;

public class AbstractNFeAdaptadorBeanTest {

    private AbstractNFeAdaptadorBean nFeAdaptadorBean;

    @Test
    public void testCalculaDV() {
        assertEquals(5, AbstractNFeAdaptadorBean.calculaDV("5206043300991100250655012000000780026730161"));
        assertEquals(0, AbstractNFeAdaptadorBean.calculaDV("0000000000000000000000000000000000000000000"));
    }

    @Test
    public void testCalculaSomaDV() {
        assertEquals(644, AbstractNFeAdaptadorBean.calculaSomaDV("5206043300991100250655012000000780026730161"));
    }

    @Test
    public void testConvertePosPeso() {
        assertEquals(2, AbstractNFeAdaptadorBean.convertePosPeso(43, 43));
        assertEquals(4, AbstractNFeAdaptadorBean.convertePosPeso(1, 43));
    }

    @Before
    public void setUp() {
        nFeAdaptadorBean = new AbstractNFeAdaptadorBean();
    }

    @Test(expected = IllegalArgumentException.class)
    public void testCalculaSomaDVWithInvalidChave() {
        AbstractNFeAdaptadorBean.calculaSomaDV("520604330099110025065501200000078002673016"); // Invalid chave length (42)
    }

}